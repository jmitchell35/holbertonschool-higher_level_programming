from os.path import exists


def generate_invitations(template:str, attendees:list):
    try:
        if not isinstance (template, str):
            raise TypeError("template must be a string")

        if not isinstance (attendees, list):
            raise TypeError("attendees must be a list")

        if len(attendees) == 0:
            raise ValueError("No data provided, no output files generated.")
      
        if len(template) == 0:
            raise ValueError("Template is empty, no output files generated.")

        keys = ['name', 'event_title', 'event_date', 'event_location']
        # Enumerate is Python good practice when needing object and index
        for i, attendee in enumerate(attendees, 1):
            if not isinstance(attendee, dict):
                raise TypeError(
                    # .__name__ to get type instead of <class type> in err msg
                    f'TypeError: list element {i}\
                        is {type(attendee).__name__}, should be dict'
                )
            invitation = template
            for key in keys:
                invitation = invitation.replace(
                    '{' + key + '}',
                    str(attendee.get(key, 'N/A'))\
                        if attendee.get(key) is not None else 'N/A'
                )

            if not exists(f'output_{i}.txt'):
                with open(f'output_{i}.txt', 'w') as f:
                     f.write(invitation)
    except TypeError as e:
        print(f"{e}")
    except ValueError as e:
        print(f"{e}")
    except Exception as e:
        print(f"Error: {e}")
