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
  
    # webcam
    webcam = Camera.from_robot(robot, "webcam")
    webcam_return_value = await webcam.get_image()
    print(f"webcam get_image return value: {webcam_return_value}")
  
    object_detection = VisionClient.from_robot(robot, "vision")

    detections = await object_detection.get_detections_from_camera('webcam')
    print(detections)
    #object_detection_return_value = await object_detection.get_classifications_from_camera(YOURCAMERANAME, 1)
    #print(f"object-detection get_classifications_from_camera return value: {object_detection_return_value}")

    # Don't forget to close the machine when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
