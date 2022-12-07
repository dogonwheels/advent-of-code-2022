import common

print(
    sum(
        [
            directory["size"]
            for directory in common.get_directories()
            if directory["size"] <= 100000
        ]
    )
)
