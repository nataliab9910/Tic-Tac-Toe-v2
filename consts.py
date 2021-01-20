"""Contains all constants used in project."""

# pylint: disable=C0301,W0511

GAME_TITLE = 'TIC-TAC-TOE Game!'

# sizes
BOARD_HEIGHT = 454
TEXT_AREA_HEIGHT = 50
SURFACE_HEIGHT = BOARD_HEIGHT + TEXT_AREA_HEIGHT
SURFACE_WIDTH = 454
LINE_WIDTH = 2
FIELD_SIZE = 150
FIELD_LINE = FIELD_SIZE + LINE_WIDTH

# centers coordinates
TEXT_AREA_CENTER = (SURFACE_WIDTH / 2, BOARD_HEIGHT + TEXT_AREA_HEIGHT / 2)
BOARD_CENTER = (SURFACE_WIDTH / 2, BOARD_HEIGHT / 2)

# board fields
FIELDS_IN_COLUMN = FIELDS_IN_ROW = 3
NUMBER_OF_FIELDS = FIELDS_IN_COLUMN * FIELDS_IN_ROW

# main game constants
NO_PLAYER, PLAYER_O, PLAYER_X, DRAW = range(4)
TEXT_AREA = 9
WRONG = -1

BOARD = [NO_PLAYER, NO_PLAYER, NO_PLAYER,
         NO_PLAYER, NO_PLAYER, NO_PLAYER,
         NO_PLAYER, NO_PLAYER, NO_PLAYER]

# @formatter:off
FIELDS_COORDINATES = [(0, 0),               (FIELD_LINE, 0),                (2 * FIELD_LINE, 0),
                      (0, FIELD_LINE),      (FIELD_LINE, FIELD_LINE),       (2 * FIELD_LINE, FIELD_LINE),
                      (0, 2 * FIELD_LINE),  (FIELD_LINE, 2 * FIELD_LINE),   (2 * FIELD_LINE, 2 * FIELD_LINE)]

FIELDS_RANGES = [
    {"x_axis": (0, FIELD_SIZE),                                "y_axis": (0, FIELD_SIZE)},
    {"x_axis": (FIELD_LINE, FIELD_LINE + FIELD_SIZE),          "y_axis": (0, FIELD_SIZE)},
    {"x_axis": (2 * FIELD_LINE, 2 * FIELD_LINE + FIELD_SIZE),  "y_axis": (0, FIELD_SIZE)},

    {"x_axis": (0, FIELD_SIZE),                                "y_axis": (FIELD_LINE, FIELD_LINE + FIELD_SIZE)},
    {"x_axis": (FIELD_LINE, FIELD_LINE + FIELD_SIZE),          "y_axis": (FIELD_LINE, FIELD_LINE + FIELD_SIZE)},
    {"x_axis": (2 * FIELD_LINE, 2 * FIELD_LINE + FIELD_SIZE),  "y_axis": (FIELD_LINE, FIELD_LINE + FIELD_SIZE)},

    {"x_axis": (0, FIELD_SIZE),                                "y_axis": (2 * FIELD_LINE, 2 * FIELD_LINE + FIELD_SIZE)},
    {"x_axis": (FIELD_LINE, FIELD_LINE + FIELD_SIZE),          "y_axis": (2 * FIELD_LINE, 2 * FIELD_LINE + FIELD_SIZE)},
    {"x_axis": (2 * FIELD_LINE, 2 * FIELD_LINE + FIELD_SIZE),  "y_axis": (2 * FIELD_LINE, 2 * FIELD_LINE + FIELD_SIZE)}
]
# @formatter:on
