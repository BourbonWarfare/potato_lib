from enum import StrEnum
from dataclasses import dataclass

class ServerStatus(StrEnum):
    UNKNOWN = 'Unknown'
    STARTING = 'Starting'
    RUNNING = 'Running'
    STOPPING = 'Stopping'
    STOPPED = 'Stopped'
    FAILED = 'Failed'


class HcStatus(StrEnum):
    UNKNOWN = 'Unknown'
    STARTING = 'Starting'
    RUNNING = 'Running'
    STOPPING = 'Stopping'
    STOPPED = 'Stopped'
    FAILED = 'Failed'
    SKIPPED = 'Skipped'  # When hc_count = 0


class StartupStatus(StrEnum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    FAILED = 'Failed'

@dataclass
class Status:
    message: str
    server_status: ServerStatus
    hc_status: HcStatus
    startup_status: StartupStatus