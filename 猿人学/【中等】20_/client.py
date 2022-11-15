import asyncio
import websockets

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def hello(message):
    # 连接 websocket 并发送消息 获取响应
    print('111111111111111111111')
    async with websockets.connect("ws://192.168.3.167:3389") as websocket:
        print('2222222222222222222222222222')
        await websocket.send(message)
        return await websocket.recv()


def get_encrypt(message):
    return str(loop.run_until_complete(hello(message)))


if __name__ == "__main__":
    print(get_encrypt(str("1")))