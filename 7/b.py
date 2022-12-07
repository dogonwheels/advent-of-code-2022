import common

directories = common.get_directories()
available_space = 70000000 - directories[0]["size"]
need_to_delete = 30000000 - available_space

print(
    sorted(
        [
            directory["size"]
            for directory in directories
            if directory["size"] >= need_to_delete
        ]
    )[0]
)
