# PowerShell command cheat sheet
## Variables

$$
Represents the last token in the last line received by the session.

$?
Represents the execution status of the last operation. It contains TRUE if the last operation succeeded and FALSE if it failed.

$^
Represents the first token in the last line received by the session.

$_
Same as $PSItem. Contains the current object in the pipeline object. You can use this variable in commands that perform an action on every object or on selected objects in a pipeline.

$ARGS
Represents an array of the undeclared parameters and/or parameter values that are passed to a function, script, or script block.

$CONSOLEFILENAME
Represents the path of the console file (.psc1) that was most recently used in the session.

$ERROR
Represents an array of error objects that represent the most recent errors.

$EVENT
Represents a PSEventArgs object that represents the event that is being processed.

$EVENTARGS
Represents an object that represents the first event argument that derives from EventArgs of the event that is being processed.

$EVENTSUBSCRIBER
Represents a PSEventSubscriber object that represents the event subscriber of the event that is being processed.

$EXECUTIONCONTEXT
Represents an EngineIntrinsics object that represents the execution context of the PowerShell host.

$FALSE
Represents FALSE. You can use this variable to represent FALSE in commands and scripts instead of using the string "false".

$FOREACH
Represents the enumerator (not the resulting values) of a ForEach loop. You can use the properties and methods of enumerators on the value of the $ForEach variable.

$HOME
Represents the full path of the user's home directory.

$HOST
Represents an object that represents the current host application for PowerShell.

$INPUT
Represents an enumerator that enumerates all input that is passed to a function.

$LASTEXITCODE
Represents the exit code of the last Windows-based program that was run.

$MATCHES
The $Matches variable works with the -match and -notmatch operators.

$MYINVOCATION
$MyInvocation is populated only for scripts, function, and script blocks. PSScriptRoot and PSCommandPath properties of the $MyInvocation

$NESTEDPROMPTLEVEL
Represents the current prompt level.

$NULL
$null is an automatic variable that contains a NULL or empty value. You can use this variable to represent an absent or undefined value in commands and scripts.

$PID
Represents the process identifier (PID) of the process that is hosting the current PowerShell session.

$PROFILE
Represents the full path of the PowerShell profile for the current user and the current host application.

$PSCMDLET
Represents an object that represents the cmdlet or advanced function that is being run.

$PSCOMMANDPATH
Represents the full path and file name of the script that is being run.

$PSCULTURE
Represents the name of the culture currently in use in the operating system.

$PSDEBUGCONTEXT
While debugging, this variable contains information about the debugging environment. Otherwise, it contains a NULL value.

$PSHOME
Represents the full path of the installation directory for PowerShell.

$PSITEM
Same as $_. Contains the current object in the pipeline object.

$PSSCRIPTROOT
Represents the directory from which a script is being run.

$PSSENDERINFO
Represents information about the user who started the PSSession, including the user identity and the time zone of the originating computer.

$PSUICULTURE
Represents the name of the user interface (UI) culture that is currently in use in the operating system.

$PSVERSIONTABLE
Represents a read-only hash table that displays details about the version of PowerShell that is running in the current session.

$SENDER
Represents the object that generated this event.

$SHELLID
Represents the identifier of the current shell.

$STACKTRACE
Represents a stack trace for the most recent error.

$THIS
In a script block that defines a script property or script method, the $This variable refers to the object that is being extended.

$TRUE
Represents TRUE. You can use this variable to represent TRUE in commands and scripts.

## Data Type

Boolean
Boolean condition
True, False

Byte
Unsigned 8-bit number
0 to 255

Sbyte
Signed 8-bit number
-128 to 127

Char
Unsigned 16-bit
U+0000 to U+ffff

DateTime
Calendar date/time
 

Decimal
128-bit decimal value, 28 – 29 significant digits
(-7.9 x 1028 to 7.9 x 1028) / (100 to 28)

Double
64-bit floating point number, 15 – 16 digits
±5.0e−324 to ±1.7e308

Int
Signed 32-bit number
-2,147,483,648 to 2,147,483,647

Uint
Unsigned 32-bit number
0 to 4,294,967,295

Long
Signed 64-bit number
9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

ULong
Unsigned 64-bit number
0 to 18,446,744,073,709,551,615

Object
any type of object
Any Object

Short
Signed 16-bit number
-32,768 to 32,767

Ushort
Unsigned 16-bit number
0 to 65,535

String
A string of characters (text)
Any text

## Operator

-eq
equals
Compares two values to be equal or not
A -eq B will give false

-ne
not equals
Compares two values to be not equal
A -ne B will give true

-gt
greater than
Compares first value to be greater than second one
B -gt A will give true

-ge
greater than or equals to
Compares first value to be greater than or equals to second one
B -ge A will give true

-lt
less than
Compares first value to be less than second one
B -lt A will give false

-le
less than or equals to
Compares first value to be less than or equals to second one
B -le A will give false



