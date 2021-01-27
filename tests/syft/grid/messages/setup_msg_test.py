# syft absolute
import syft as sy
from syft.core.io.address import Address
from syft.grid.messages.setup_messages import CreateInitialSetUpMessage
from syft.grid.messages.setup_messages import CreateInitialSetUpResponse
from syft.grid.messages.setup_messages import GetSetUpMessage
from syft.grid.messages.setup_messages import GetSetUpResponse


def test_create_initial_setup_message_serde() -> None:
    bob_vm = sy.VirtualMachine(name="Bob")
    target = Address(name="Alice")

    request_content = {
        "settings": {
            "cloud-admin-token": "d84we35ad3a1d59a84sd9",
            "cloud-credentials": "<cloud-credentials.pem>",
            "infra": {"autoscaling": True, "triggers": {"memory": "50", "vCPU": "80"}},
        }
    }
    msg = CreateInitialSetUpMessage(
        address=target,
        content=request_content,
        reply_to=bob_vm.address,
    )

    blob = msg.serialize()
    msg2 = sy.deserialize(blob=blob)

    assert msg.id == msg2.id
    assert msg.address == target
    assert msg.content == msg2.content
    assert msg == msg2


def test_create_initial_setup_response_serde() -> None:
    target = Address(name="Alice")

    request_content = {"msg": "Initial setup registered successfully!"}
    msg = CreateInitialSetUpResponse(
        address=target,
        success=True,
        content=request_content,
    )

    blob = msg.serialize()
    msg2 = sy.deserialize(blob=blob)

    assert msg.id == msg2.id
    assert msg.address == target
    assert msg.content == msg2.content
    assert msg == msg2


def test_get_initial_setup_message_serde() -> None:
    bob_vm = sy.VirtualMachine(name="Bob")
    target = Address(name="Alice")

    request_content = {}
    msg = GetSetUpMessage(
        address=target,
        content=request_content,
        reply_to=bob_vm.address,
    )

    blob = msg.serialize()
    msg2 = sy.deserialize(blob=blob)

    assert msg.id == msg2.id
    assert msg.address == target
    assert msg.content == msg2.content
    assert msg == msg2


def test_delete_worker_response_serde() -> None:
    target = Address(name="Alice")

    content = {
        "settings": {
            "cloud-admin-token": "d84we35ad3a1d59a84sd9",
            "cloud-credentials": "<cloud-credentials.pem>",
            "infra": {"autoscaling": True, "triggers": {"memory": "50", "vCPU": "80"}},
        }
    }
    msg = GetSetUpResponse(
        success=True,
        address=target,
        content=content,
    )

    blob = msg.serialize()
    msg2 = sy.deserialize(blob=blob)

    assert msg.id == msg2.id
    assert msg.address == target
    assert msg.content == msg2.content
    assert msg == msg2