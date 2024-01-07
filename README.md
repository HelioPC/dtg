# Dummy data generator (dtg) 🤡 🎲

## Usage

```
usage: dtg [-v | --version] [-h | --help] <command> [args]
```

(dtg) A command line utility to generate dummy data. dtg has 4 commands to use, which are:

- init: Initialize a dtg repository
```
dtg init
```

---

- create: Creates a dummy data model
```
dtg create modelname [--fields=field:type]
```

---

- add: Adds (a) field(s) to the dummy data model
```
dtg add field:type modelname
```

---

- show: Shows all dummy data models
```
dtg show modelname
```

- generate: Generates dummy data based on the dummy data model
```
dtg generate modelname [--count=number] [--output=file]
```

### NOTE: More commands will be idealized and later added to the project. So, currently this is just an idealization of what the project will become. 🚧⛔️💻
