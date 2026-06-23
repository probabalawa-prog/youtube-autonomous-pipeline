import asyncio
import edge_tts

async def main():
    with open("input/script.txt", "r", encoding="utf-8") as f:
        text = f.read()

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-GuyNeural"
    )

    await communicate.save("output/audio.mp3")
    print("Audio generated successfully!")

asyncio.run(main())