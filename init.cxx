#include "init.hxx"
#include "dir_struct.hxx"


bool 
init_dir_i (char* dir2, logger *new_instance)
{
    bool            success;
    success = true;

    // fs::path parent_loc = dir1;
    // success = success & fs::create_directories (dir1);
    
    dir_struct dir = dir_struct(dir2, new_instance);

    for (auto it: dir.get_files())
    {
        cout << it.get_path().string() << "\n";
    }

    return success;
}
