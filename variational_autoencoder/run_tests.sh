#!/bin/bash
test_dir="tests/"

coverage run -m pytest $test_dir -s
coverage html
