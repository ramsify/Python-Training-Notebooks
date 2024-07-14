"""
Removing directories
rmdir() function similar to that of mkdir() except for that it's used to
 remove/delete a base/leaf directory
removedirs() function is used to delete the subdirectories along with the
base/leaf directory, if the subdirectories are empty after
deleting/removing the base/leaf directory.
In case the subdirectories are having other files or folders they won't be impacted

Both the functions would throw error if we try to remove a base/leaf directory
that doesn't exist or if any of the subdirectories doesn't exist

Note: Both these functions are used to remove only the empty directories.
Even the removedirs() function will throw an error if you try to delete a
non-empty base/leaf directory
"""
import os

cwd = os.getcwd()
print(cwd)

# rmdir()
sub_path = 'Dir_1/sub_dir_1/leaf_dir_2' # removes the leaf_dir_2
os.rmdir(os.path.join(cwd, sub_path))

# removedirs()
sub_path1 = 'Dir_1/sub_dir_1/leaf_dir_1'
sub_path2 = 'Dir_1/sub_dir_2/leaf_dir_1'
mypath1 = os.path.join(cwd, sub_path1)
mypath2 = os.path.join(cwd, sub_path2)

'''
removedirs() in the below code does the following:
1. removes both sub_dir_1 and leaf_dir_1 as sub_dir_1 has no other content inside
2. removes only leaf_dir_1 but sub_dir_2 will not be removed as it has
another child directory leaf_dir_2
'''
for path in [sub_path1, sub_path2]:
    os.removedirs(path)
    print('The Paths have been removed successfully')

