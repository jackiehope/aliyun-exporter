from aliyunsdkcore.client import AcsClient
from cachetools import cached, TTLCache
from prometheus_client.metrics_core import GaugeMetricFamily

'''
info provider provide the information of cloud resources
'''
class InfoProvider():

    def __init__(self, client: AcsClient):
        self.cache = TTLCache(maxsize=100, ttl=3600)
        self.client = client

    def getMetrics(self, resource: str) -> GaugeMetricFamily:
        return {
            'ecs': self.ecsInfo(),
            'rds': self.rdsInfo(),
            'redis': self.redisInfo(),
        }[resource]

    def ecsInfo(self) -> GaugeMetricFamily:
        pass

    def rdsInfo(self) -> GaugeMetricFamily:
        pass

    def redisInfo(self) -> GaugeMetricFamily:
        pass

