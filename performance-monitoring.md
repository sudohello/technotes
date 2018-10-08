---
title: Performance Monitoring
---

**Table of Contents**
* TOC
{:toc}


## Performance Monitoring

**Ubuntu**
* vmstat, iostat
- https://www.thegeekstuff.com/2011/07/iostat-vmstat-mpstat-examples/


## GPU Monitoring
* https://unix.stackexchange.com/questions/38560/gpu-usage-monitoring-cuda
* https://github.com/wookayin/gpustat
* https://github.com/mountassir/gmonitor
```bash
nvidia-smi -l 1
watch -n 1 nvidia-smi
watch -n0.1 "nvidia-settings -q GPUUtilization -q useddedicatedgpumemory"
#
nvidia-smi --help-query-gpu
nvidia-smi --format=csv --query-gpu=power.draw,utilization.gpu,fan.speed,temperature.gpu
watch -n 1 nvidia-smi --format=csv --query-gpu=power.draw,utilization.gpu,fan.speed,temperature.gpu
#
sudo fuser -v /dev/nvidia*
```