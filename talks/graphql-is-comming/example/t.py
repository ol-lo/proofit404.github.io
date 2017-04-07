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


# j("""
# {
#   viewer {
#     firstName
#   }
# }
# """)

j('''
query {
  tasks {
    title
  }
}
''')

j('''
query {
  task(id: 1) {
    title
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
    ...EmpAttrs
    subordinates {
      ...EmpAttrs
      subordinates {
        ...EmpAttrs
        subordinates {
          ...EmpAttrs
        }
      }
    }
  }
}

fragment EmpAttrs on Employee {
  firstName
  assignedTasks {
    title
    statusHistory {
      name
    }
    comments {
      author {
        firstName
      }
      text
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
