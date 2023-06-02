from typing import Union


class TaskReport:
    SEPERATOR = " ; "
    PREFIX = ""

    def __init__(self,
                 name: str,
                 times: Union[list[float], float],
                 count: int,
                 ratio: float,
                 children: list["TaskReport"],
                 padding_name: int):
        self.name = name
        self.times = times if isinstance(times, list) else [times]
        self.count = count
        self.ratio = ratio
        self.children = children

        self.internal_time = None

        self.padding_name = padding_name

    @property
    def avg_duration(self):
        return sum(self.times) / len(self.times)

    @property
    def total_duration(self):
        return sum(self.times)

    def print(self, prefix="", spacing=0, skip_first=False):
        if not skip_first:
            print(self.__str__())

        if self.children:
            for i, child in enumerate(self.children):
                if i == len(self.children) - 1 or len(child.children) > 1:
                    print(" " * spacing + f"└── {child}")
                    if child.children:
                        child.print(prefix=prefix + " ", spacing=spacing + 4, skip_first=True)
                else:
                    print(" " * spacing + f"├── {child}")
                    if child.children:
                        child.print(prefix=prefix + "│", spacing=spacing + 4, skip_first=True)

        if self.internal_time is not None:
            internal_time = self.internal_time
            internal_time_ratio = self.internal_time / self.total_duration

            # change unit to ms if internal time is too small, if still too small, change to us
            unit = "seconds"
            if internal_time < 0.00001:
                internal_time *= 1000000
                unit = "microseconds"
            elif internal_time < 0.01:
                internal_time *= 1000
                unit = "milliseconds"

            print(" " * spacing + f"└── [{internal_time_ratio:.2%}%] internal time: {internal_time:.5f} {unit}")
    @classmethod
    def from_dict(cls, task_report_dict: dict, padding_name=0):
        padding_children = 0
        children = []
        if "subtasks" in task_report_dict:
            for child in task_report_dict["subtasks"].values():
                padding_children = max(padding_children, len(child["name"]))
                children.append(cls.from_dict(child, padding_name=padding_children))

        return cls(
            name=task_report_dict["name"],
            times=task_report_dict["times"],
            count=task_report_dict["count"],
            ratio=task_report_dict["ratio"],
            children=children,
            padding_name=padding_name
        )

    def __str__(self):

        name_str = f"{self.name:{self.padding_name}}" if self.padding_name > 0 else self.name

        to_print = [
            f"[{self.ratio:.2%}%] {name_str}",
            f"{self.total_duration:6.5f} seconds",
            f"{self.count} times",
            f"avg {self.avg_duration:6.5f} seconds"
        ]

        if self.PREFIX != "":
            to_print.insert(0, self.PREFIX)

        return TaskReport.SEPERATOR.join(to_print)

    def __repr__(self):
        return self.__str__()
