import json
import logging
import socket

import azure.functions as func

import text_server.interpreter as interp

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    uuid = req.params.get('uuid')
    transcript = req.params.get('transcript')
    server = req.params.get('server')
    if not uuid or not transcript or not server:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            uuid = req_body.get('uuid')
            transcript = req_body.get('transcript')
            server = req_body.get('server')

    if uuid and transcript and server:
        socket.setdefaulttimeout(5.0)
        sending_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_s = server.split(':')
        try:
            sending_sock.connect((server_s[0], int(server_s[1]) if len(server_s) == 2 else 5003))
        except (socket.timeout, TimeoutError):
            return func.HttpResponse(f"Hello, {uuid}, we failed to connect to {server}. This HTTP triggered function executed successfully.", status_code=200)

        command = interp.process_instruction(transcript)
        if command is None:
            sending_sock.close()
            return func.HttpResponse(f"Hello, {uuid}, we failed to parse \"{transcript}\". This Http triggered function executed successfully.", status_code=200)
        
        command['client_name'] = uuid
        sending_sock.send((json.dumps(command) + "\n").encode())
        sending_sock.close()      
        return func.HttpResponse(f"Hello, {uuid}, we've sent {command} to {server}. This HTTP triggered function executed successfully.", status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a uuid, transcript, and server in the query string or in the request body.",
             status_code=200
        )
