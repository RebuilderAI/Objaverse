import open3d as o3d
import trimesh
import os
import glob
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Parser for voxelization of GLB')
parser.add_argument('--dir', type=str)
parser.add_argument('--index', type=int)

args = parser.parse_args()


def voxelization(glb_file_path, voxel_size):
    # Read GLB file
    mesh = o3d.io.read_triangle_mesh(glb_file_path)

    # Compute the axis-aligned bounding box (AABB) of the mesh
    # aabb = mesh.get_axis_aligned_bounding_box()

    # Voxelization
    voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh, voxel_size=voxel_size)

    return voxel_grid

if __name__ == "__main__":
    # Path to the GLB file
    glb_file_path = glob.glob(os.path.join(str(args.dir), "*.glb" ))
    idx = args.index
    print(glb_file_path)
    # Voxel size (size of each voxel in the grid)
    voxel_size = 0.05  # Adjust this according to your requirements

    # Voxelization
    voxel_grid = voxelization(glb_file_path[idx], voxel_size)

    # Visualize the voxel grid
    o3d.visualization.draw_geometries([voxel_grid])