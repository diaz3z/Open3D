import open3d as o3d

# Load the point cloud file
point_cloud = o3d.io.read_point_cloud("data\samp21-utm-ground.pcd")  # Use your file path



downsampled_pcd = point_cloud.voxel_down_sample(voxel_size=0.05)

# plane_model, inliers = downsampled_pcd.segment_plane(distance_threshhold = 0.01,
#                                                      ransac_n = 3,
#                                                      num_iterations = 1000)

# plane_cloud = downsampled_pcd.select_by_index(inliers)


# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])