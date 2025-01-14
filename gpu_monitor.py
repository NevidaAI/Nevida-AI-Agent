import pynvml

class GPUMonitor:
    def __init__(self):
        pynvml.nvmlInit()

    def get_gpu_metrics(self):
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # Single GPU system example
        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        power_draw = pynvml.nvmlDeviceGetPowerUsage(handle)
        return {
            "temperature": temperature,
            "gpu_utilization": utilization.gpu,
            "power_draw": power_draw / 1000  # Convert mW to W
        }

if __name__ == "__main__":
    monitor = GPUMonitor()
    print(monitor.get_gpu_metrics())
