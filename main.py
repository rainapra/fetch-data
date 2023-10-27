import json
from datetime import datetime

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from app.config import POSTGRES_CONNECTION
from app.postgres import insert_to_postgres
from app.mask_pii import mask_pii_fields
from app.sqs import read_messages_from_sqs
from app.utils import mask_data
from app.utils import mask_pii_data
from app.mask_pii import mask_pii_data


@dataclass
class Record:
    user_id: str
    device_type: str
    masked_ip: str
    masked_device_id: str
    locale: str
    app_version: str


def create_record(masked_data: Dict[str, Any]) -> Optional[Record]:
    if masked_data is None:
        return None

def process_messages(messages: List[Dict[str, Any]]) -> List[Tuple]:
    return Record(
        user_id=masked_data["user_id"],
        device_type=masked_data["device_type"],
        masked_ip=masked_data["masked_ip"],
        masked_device_id=masked_data["masked_device_id"],
        locale=masked_data["locale"],
        app_version=masked_data["app_version"],
    )
def process_messages(messages: List[Dict[str, Any]]) -> List[Record]:
    records = []

    for message in messages:
        data = json.loads(message["Body"])
        masked_data = mask_pii_data(data)
        record = create_record(masked_data)

        record = (
            masked_data["user_id"],
            masked_data["device_type"],
            masked_data["masked_ip"],
            masked_data["masked_device_id"],
            masked_data["locale"],
            masked_data["app_version"],
            masked_data["create_date"],
        )
        records.append(record)
        if record is not None:
            records.append(record)

    return records


def main():
    messages = read_messages_from_sqs()
    print(f"Messages: {messages}")

    records = process_messages(messages)
    print(f"Records: {records}")

    insert_to_postgres(POSTGRES_CONNECTION, records)