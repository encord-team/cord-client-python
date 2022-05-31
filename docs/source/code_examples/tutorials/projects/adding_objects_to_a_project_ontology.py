from encord import EncordUserClient, ProjectManager
from encord.project_ontology.object_type import ObjectShape

user_client: EncordUserClient = EncordUserClient.create_with_ssh_private_key("<your_private_key>")
project_manager: ProjectManager = user_client.get_project_manager("<project_hash>")

success: bool = project_manager.add_object("Dog", ObjectShape.BOUNDING_BOX)
print(success)
