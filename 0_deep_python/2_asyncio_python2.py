import asyncio

# define a coroutine that simulates a time-consuming task
async def fetch_(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) # simulate an I/O operation with a sleep 
    print("Data fetched")
    return {"data": "Some data"} # Return some data

# define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    fetch_data = fetch_(2) # Corrected assignment
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await fetch_data  # Corrected await
    print(f"Received result: {result}")
    print("End of main coroutine")
    
    
# Run the main coroutine
asyncio.run(main())
