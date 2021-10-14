EXP_GROUPS = {}

EXP_GROUPS["mnist"] = []
for lr in [1]:
    EXP_GROUPS["mnist"] += [{"lr": lr, "dataset": "mnist", "model": "linear"}]

# EXP_GROUPS["visual"] = []
# for lr in [1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
#     EXP_GROUPS["visual"] += [{"lr": lr, "dataset": "visual", "model": "linear"}]
