from fastapi import FastAPI, HTTPException
from optimizer import GPUOptimizer
from gpu_monitor import GPUMonitor
from pydantic import BaseModel

app = FastAPI()

# Initialize GPU Monitor and Optimizer
monitor = GPUMonitor()
optimizer = GPUOptimizer(target_performance=90, power_limit=200)

# Data Model for Optimization Request
class OptimizationRequest(BaseModel):
    target_performance: int
    power_limit: int

@app.get("/api/metrics")
def get_metrics():
    try:
        metrics = monitor.get_gpu_metrics()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching GPU metrics: {e}")

@app.post("/api/optimize")
def optimize_performance(request: OptimizationRequest):
    try:
        metrics = monitor.get_gpu_metrics()
        optimizer.target_performance = request.target_performance
        optimizer.power_limit = request.power_limit
        suggestion = optimizer.optimize(list(metrics.values()))
        return {"suggestion": suggestion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error optimizing performance: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
