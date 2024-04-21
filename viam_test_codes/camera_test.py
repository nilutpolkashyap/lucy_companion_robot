import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.camera import Camera
from viam.components.board import Board


async def connect():
    opts = RobotClient.Options.with_api_key( 
        api_key='<API_KEY>',
        api_key_id='<API_KEY_ID>'
    )
    return await RobotClient.at_address('lucy-robot-main.l48ztb9x2e.viam.cloud', opts)

async def main():
    machine = await connect()

    print('Resources:')
    print(machine.resource_names)
    
    # webcam
    webcam = Camera.from_robot(machine, "webcam")
    webcam_return_value = await webcam.get_image()
    print(f"webcam get_image return value: {webcam_return_value}")

    # Don't forget to close the machine when you're done!
    await machine.close()

if __name__ == '__main__':
    asyncio.run(main())
