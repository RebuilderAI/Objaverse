data_extraction.ipynb is the code that is used to extract the objaverse 1.0 3d model dataset. The data is in glb. format, and each also has metadata that describes each file's license, category, etc. 

reprocess.ipynb is the code that is used to get all the dataframes of the objects and metadata that have been extracted so far. You can use it to obtain partial object data from it.

voxel_open3d.py & voxel_open3d.ipynb are codes that are used to voxelize 3D models. The libraries used for it are Trimesh to first convert .glb data into mesh and later on the mesh is voxelized with Open3D.
