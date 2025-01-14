from fastapi import FastAPI
from gpu_monitor import GPUMonitor
from logger import logger

app = FastAPI()
monitor = GPUMonitor()

@app.get("/gpu/diagnostics")
async def gpu_diagnostics():
    try:
        metrics = monitor.get_diagnostics()
        logger.info("Diagnostics fetched successfully.")
        return {"status": "success", "diagnostics": metrics}
    except Exception as e:
        logger.error(f"Error fetching diagnostics: {str(e)}")
        return {"status": "error", "message": str(e)}

@app.get("/gpu/stress-test")
async def gpu_stress_test(duration: int = 60):
    try:
        result = monitor.run_stress_test(duration)
        logger.info("Stress test completed.")
        return {"status": "success", "result": result}
    except Exception as e:
        logger.error(f"Stress test failed: {str(e)}")
        return {"status": "error", "message": str(e)}
