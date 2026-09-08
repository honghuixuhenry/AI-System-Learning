from dataclasses import dataclass


@dataclass
class NetworkMetrics:
    latency_ms: float
    bandwidth_mbps: float
    throughput_mbps: float
    jitter_ms: float
    packet_loss_rate: float


def utilization(
    metrics: NetworkMetrics
) -> float:

    if metrics.bandwidth_mbps == 0:
        return 0.0

    return (
        metrics.throughput_mbps
        /
        metrics.bandwidth_mbps
    )