#!/usr/bin/env bash

chmod +x task_* tests/tests.sh

ln -s /wg_test_tasks/task_1.py /usr/local/bin/task1
ln -s /wg_test_tasks/task_2.py /usr/local/bin/task2
ln -s /wg_test_tasks/task_3.py /usr/local/bin/task3
ln -s /wg_test_tasks/task_4.py /usr/local/bin/task4
ln -s /wg_test_tasks/task_4.py /usr/local/bin/task5

ln -s /wg_test_tasks/tests/tests.sh /usr/local/bin/tests

ln -s /wg_test_tasks/extra/clear.py /usr/local/bin/clear
ln -s /wg_test_tasks/extra/info.py /usr/local/bin/info
