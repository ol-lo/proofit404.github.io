import json
from itertools import count

from taskmanager.schema import schema

counter = count(1)


def j(request):
    num = next(counter)
    print('\n#%d\n' % num)
    result = schema.execute(request)
    print(json.dumps(result.data, indent=2))
    print(json.dumps(result.errors, indent=2))


j('''
query {
  tasks {
    title
  }
}
''')

j('''
query {
  task(id: "VGFzazox") {
    title
  }
}
''')

j('''
query {
  allTasks {
    edges {
      node {
        id
        title
      }
    }
  }
}
''')

j('''
query {
  allTasks(title_Startswith: "to") {
    edges {
      node {
        id
        title
      }
    }
  }
}
''')

j('''
{
  employees {
    firstName
  }
}
''')

j('''
{
  employees {
    firstName
    subordinates {
      firstName
    }
  }
}
''')

j('''
{
  employees {
    firstName
    subordinates {
      firstName
        subordinates {
          firstName
          subordinates {
            firstName
          }
        }
    }
  }
}
''')

j('''
{
  tasks {
    title
    createdBy {
      firstName
      subordinates {
        firstName
      }
    }
  }
}
''')

j('''
{
  employees {
    firstName
  }
  tasks {
    title
  }
}
''')

j('''
{
  tasks(limit: 1) {
    title
  }
}
''')
