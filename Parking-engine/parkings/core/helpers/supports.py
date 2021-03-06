from parkings.core.commands import Command, EXC_NOT_FOUND_INT
from parkings.models.spaces import CarSlots

class FormatSupport():

    def format_start_new_output(self, resp):
        OUT_SKELETON = "Created a parking lot with {} slots"
        FAIL_CREATE_ERROR_MSG = "Failed to create a parking lot"

        if resp == EXC_NOT_FOUND_INT:
            success = False
            return success, FAIL_CREATE_ERROR_MSG

        success = True
        return success, OUT_SKELETON.format(resp)

    def format_park_output(self, resp):
        OUT_SKELETON = "Allocated slot number: {}"
        FULL_EXC_MSG = "Sorry, parking lot is full"

        if resp == EXC_NOT_FOUND_INT:
            success = False
            return success, FULL_EXC_MSG

        success = True
        return success, OUT_SKELETON.format(resp)

    def format_leave_output(self, resp):
        OUT_SKELETON = "Slot number {} is free"
        ERROR_MSG = "Slot number is already empty"

        if resp == EXC_NOT_FOUND_INT:
            success = False
            return success, ERROR_MSG.format(resp)

        success = True
        return success, OUT_SKELETON.format(resp)

    def format_status_output(self, resp):
        OUT_SKELETON = "{:<12}{:19}{}"
        OUT_HEADER = OUT_SKELETON.format("Slot No.", "Registration No", "Colour")
        output = [OUT_HEADER]

        for slot_id, regnum, color in resp:
            output.append(OUT_SKELETON.format(slot_id, regnum, color))

        success = True
        return success, "\n".join(output)

    def format_query_single_output(self, resp):
        NOT_FOUND_MSG = "Not found"
        if resp and resp != EXC_NOT_FOUND_INT:
            success = True
            return success, resp

        return False, NOT_FOUND_MSG

    def format_query_many_output(self, resp):
        NOT_FOUND_MSG = "Not found"
        if resp:
            resp = [str(item) for item in resp]
            success = True
            return success, ", ".join(resp)

        return False, NOT_FOUND_MSG
