#pragma once

#include <bits/stdc++.h>
#include <boost/filesystem.hpp>
#include "file.hxx"
#include <archive.h>
#include <archive_entry.h>
#include "log.hxx"
#include "json.hxx"

namespace fs = boost::filesystem;
using namespace std;
using json = nlohmann::json;

typedef vector <fs::path> vec;


class dir_struct
{   
    intmax_t                    dir_size;
    logger                      *log;
    vector <file_data>          files,
                                mod_files;
    fs::path                    loc;
    string                      commit_message;
    time_t                      commit_time;


    void                        get_files_from_dir_h (fs::path p,
                                                      vector<file_data> &files);
    void                        add_file (fs::path p,
                                           vector<file_data> &files);     
    vector <file_data>          get_new_files (vector<file_data> &previous_files);  

    public:
    dir_struct                  ();
    dir_struct                  (fs::path dir, logger *log);
    dir_struct                  (json obj);
    
    intmax_t                    get_dir_size ();
    void                        save_files (int version_no);
    void                        load_files (int Version_no);
    void                        set_mod_files (vector<file_data> &mod_files);
    void                        set_commit_message (string message);
    string                      get_commit_message ();
    void                        set_commit_time (time_t t);
    time_t                      get_commit_time ();
    vector <file_data>          get_files ();
    vector <file_data>          get_mod_files (vector <file_data> prev_version);
    vector <file_data>          get_status ();
    vector <file_data>          get_files_from_dir (fs::path p);
    json                        dump_dir_struct ();

};