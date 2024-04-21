import asyncio

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

    print('Resources:')
    print(robot.resource_names)

    speech = SpeechService.from_robot(robot, name="speech")
    while True:
        commands = await speech.get_commands(1)
        print(commands)
        await asyncio.sleep(3)

    # Don't forget to close the machine when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
