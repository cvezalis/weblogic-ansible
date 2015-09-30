#!/bin/bash

if [ $USER = "{{ oracle_user }}" ]; then
  if [ $SHELL = "/bin/ksh" ]; then
    ulimit -p {{ hard_nproc }}
    ulimit -n {{ hard_no_file }}
  else
    ulimit -u {{ hard_nproc }} -n {{ hard_no_file }}
  fi
fi