#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "David Guzman with help from Gordon"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    path_of_dirname = []
    for dirpath, _, filenames in os.walk(os.path.abspath(dirname)):
        for files in filenames:
            file_pattern = re.findall(r'__\w+__', files)
            if file_pattern:
                path_of_dirname.append(os.path.join(dirpath, files))
        break
    return path_of_dirname


def is_directory(path):
    """Checks if it's a directory"""
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except OSError:
            print(f"You failed to create this {path}")
            return False
    return True


def copy_to(path_list, dest_dir):
    """Copies Files"""
    directory_status = is_directory(dest_dir)
    if not directory_status:
        return
    for files in path_list:
        shutil.copyfile(files, os.path.join(dest_dir, os.path.basename(files)))


def zip_to(path_list, dest_zip):
    """Gives a command"""
    command = ['zip', '-j', dest_zip]
    command.extend(path_list)
    print(" ".join(command))
    subprocess.call(command)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='Grab special files from the dir')
    ns = parser.parse_args(args)
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    path_list = get_special_paths(ns.from_dir)

    for path in path_list:
        print(path)

    if ns.todir:
        copy_to(path_list, ns.todir)
    if ns.tozip:
        zip_to(path_list, ns.tozip)


if __name__ == "__main__":
    main(sys.argv[1:])
