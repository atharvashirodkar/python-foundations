# Authentication System Flow

## Input

Select option by entering respective number:

1. Sign-In
2. Sign-Up

---

## Sign-In Flow

```text
# User enters "1"

Username: Andy
Password: Andy123
```

### Backend Logic

- Check whether the username exists.
- If the username does not exist, show:

```text
Username is wrong.
```

- If the username exists, check the password.
- If the password is incorrect, show:

```text
Your password is incorrect.
```

- If both username and password are correct, show:

```text
Welcome to the system.
```

---

## Sign-Up Flow

```text
# User enters "2"
```

### Username Validation

```text
Username: Andy
```

- Check whether the username already exists.
- If the username already exists, show:

```text
This username is already taken. Please choose a different username.
```

- Show the username input field again until a unique username is entered.

### Password Creation

```text
Password: Andy1234
```

- Save the username and password.
- After successful registration, show:

```text
Welcome! Your account has been successfully created.
```