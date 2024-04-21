import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.camera import Camera
from viam.components.board import Board


async def connect():
    opts = RobotClient.Options.with_api_key( 
        api_key='syzxne67tsxdy1198k0tkjp3pci74jnx',
        api_key_id='cf8af789-016b-4b46-bbf4-52fb60ac50ab'
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
