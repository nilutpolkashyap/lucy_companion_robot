import asyncio
import re
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.board import Board
from viam.components.camera import Camera
from viam.services.vision import VisionClient
from speech_service_api import SpeechService
from chat_service_api import Chat
from datetime import datetime

async def connect():
    opts = RobotClient.Options.with_api_key( 
        api_key='<API_KEY>',
        api_key_id='<API_KEY_ID>'
    )
    return await RobotClient.at_address('lucy-robot-main.l48ztb9x2e.viam.cloud', opts)

async def main():
    robot = await connect()

    llm = Chat.from_robot(machine, name="llm")
    speech = SpeechService.from_robot(robot, name="speech")
    object_detection = VisionClient.from_robot(robot, "vision")

    detectedObject = ""
    
    while True:
        detections = await object_detection.get_detections_from_camera('webcam')

        if len(detections) > 0:
            detectedObject = detections[0].class_name

        commands = await speech.get_commands(1)

        if len(commands) > 0:
            command = commands[0]
            print(detections[0].class_name)

            if detectedObject != "":
                article = "an" if detectedObject[0].lower() in 'aeiou' else "a"

                initialCommand = "I can see"
                initialResult = f"{initialCommand} {article} {detectedObject}."
                print(initialResult)

                await speech.say(initialResult, True)

                article = "an" if detectedObject[0].lower() in 'aeiou' else "a"

                command = re.sub(r'(this|that|the) object',  f"{article} {detectedObject}", command)

                response = await llm.chat(command)
                print(response)

                await speech.say(response, True)

        # await asyncio.sleep(3)

    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
