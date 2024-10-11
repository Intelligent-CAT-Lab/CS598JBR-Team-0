###################################################################
# This is a list of all commands you need to run for MP3 on Colab.
###################################################################

# TODO: Update Your NetIDs in alphabetical order
NetIDs = ["sampleID1", "sampleID2", "sampleID3", "sampleID4"]
NetIDs_str = " ".join(NetIDs)

# TODO: Clone your GitHub repository
! git clone [Your GitHub Link]
%cd [Your GitHub Repo]

# Set up requirements for dataset generation

# dataset generation
! python3 MP3/codenet_dataset_generation.py {NetIDs_str} |& tee codenet_dataset_generation.log

seed = "<your_seed>"
# TODO: Replace the file path of selected_codenet_[seed].jsonl generated in previous step
input_dataset = "selected_codenet_" + seed + ".jsonl"

# Set up requirements for model prompting
! bash -x MP1/setup_models.sh

task_1_response = "task_1_response_" + seed + ".jsonl"
task_1_evaluation = "task_1_evaluation_" + seed + ".jsonl"

# Task 1
! python3 MP3/task_1.py {input_dataset} {task_1_response} "True" |& tee task_1.log
! python3 MP3/evaluation_translation.py {task_1_response} {task_1_evaluation} |& tee task_1_evaluation.log

# Task 2

%cd ..

# git push all nessacery files (e.g., *jsonl, *log) to your GitHub repository
