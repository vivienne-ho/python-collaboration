#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:24:07 2024

@author: vivienneho
"""

def main():
    to_do = []
    completed_tasks = []
    action = input("Would you like to add new tasks, view all tasks, mark tasks as completed, or delete tasks? ")
    if action == "add":
        add_task(to_do)
    if action == "view":
        view_tasks()
    if action == "mark":
        task = input("What task do you want to mark as completed? ")
        mark_completed(task, to_do, completed_tasks)
    if action == "delete":
        task = input("What task do you want to delete?")
        
#===================================================================
    
def add_task(to_do):
    task = input("What task do you want to add? ")
    to_do.append(task)
    
#===================================================================
    
def view_tasks(to_do):
    print(to_do)
    
#===================================================================
    
def mark_completed(task, to_do, completed_tasks):
    to_do.remove(task)
    completed_tasks.append(task)
    
#===================================================================
    
def delete_task(task, to_do):
    to_do.remove(task)
    
#===================================================================

main()
