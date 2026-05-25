from huggingface_hub import login, HfApi

# (optional) Login with your Hugging Face credentials
login(token="<your-token-here>")

api = HfApi()
# api.create_repo(repo_id="", repo_type="model", exist_ok=True)
# api.create_repo(repo_id="", repo_type="dataset", exist_ok=True)

#specific file to upload 
-- Dataset
api.upload_file(
    path_or_fileobj="<your-file>",
    path_in_repo="<your-file>",
    repo_id="<your-repo-id>",
    repo_type="dataset",
)

-- Model
api.upload_file(
    path_or_fileobj="<your-file>",
    path_in_repo="<your-file>",
    repo_id="<your-repo-id>",
    repo_type="model",
)

#specific folder to upload 
-- Dataset
api.upload_folder(
    folder_path="<your-folder>",
    repo_id="<your-repo-id>",
    repo_type="dataset",
)

-- Model
api.upload_folder(
    folder_path="<your-folder>",
    repo_id="<your-repo-id>",
    repo_type="model",
)
