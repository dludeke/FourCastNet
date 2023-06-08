import h5py

def analyze_h5_dataset(file_path, dataset_name):
    # Open the h5 file
    with h5py.File(file_path, 'r') as f:
        # Check if the dataset exists
        if dataset_name not in f:
            print(f"Dataset '{dataset_name}' not found in the file.")
            return
        
        # Access the dataset
        dataset = f[dataset_name]
        
        # Print dataset information
        print(f"Dataset name: {dataset_name}")
        print(f"Shape: {dataset.shape}")
        print(f"Dtype: {dataset.dtype}")
        
        # Perform further analysis as needed
        # ...

# Specify the file path and dataset name
file_path = '/home/ubuntu/train/1980_u10_500ts.h5'
dataset_name = 'small'

# Call the analyze_h5_dataset function
analyze_h5_dataset(file_path, dataset_name)
