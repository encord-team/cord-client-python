from dataclasses import dataclass
from enum import Enum, auto
from typing import Iterable
from uuid import UUID

from encord.orm.workflow import Workflow as WorkflowORM
from encord.orm.workflow import WorkflowStageType


class Task:
    task_uuid: UUID


@dataclass(frozen=True)
class WorkflowStage:
    stage_type: WorkflowStageType
    uuid: UUID
    title: str

    def __repr__(self):
        return f"WorkflowStage(stage_type={self.stage_type} uuid='{self.uuid}' title='{self.title}')"


class Workflow:
    stages: list[WorkflowStage] = []

    def __init__(self, workflow_orm: WorkflowORM):
        self.stages = [WorkflowStage(uuid=x.uuid, title=x.title, stage_type=x.node_type) for x in workflow_orm.stages]

    def get_stage(self, *, name: str | None = None, uuid: UUID | None = None) -> WorkflowStage:
        for stage in self.stages:
            if (uuid is not None and stage.uuid == uuid) or (name is not None and stage.title == name):
                return stage

        raise ValueError(f"No matching stage found: '{uuid or name}'")
