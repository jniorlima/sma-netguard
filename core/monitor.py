from ping3 import ping
import psutil

class NetworkMonitor:

    def get_ping(self, host):

        try:

            latency = ping(host, timeout=1)

            if latency is None:
                return None

            return latency * 1000

        except:

            return None


    def get_network_usage(self):

        net = psutil.net_io_counters()

        return {

            "bytes_sent": net.bytes_sent,

            "bytes_recv": net.bytes_recv,

            "packets_sent": net.packets_sent,

            "packets_recv": net.packets_recv

        }