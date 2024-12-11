#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include "../raylase_includes/include/ClientAPI.h"

#define CARD_IP "192.168.1.141"

static rlResult markSquare(rlHandle handle);
static int printLastError(void);

int main()
{
    rlHandle handle = rlConnect(CARD_IP, 49374);
    if (handle < 0)
        return printLastError();

    rlResult status;

    if ((status = rlSystemResetToDefaults(handle)) != rlSUCCESS)
        goto Cleanup;

    rlLaserConfig lc;
    if ((status = rlLaserGetConfig(handle, &lc)) != rlSUCCESS) goto Cleanup;
    lc.PowerScale = 0.25;
    if ((status = rlLaserSetConfig(handle, &lc)) != rlSUCCESS) goto Cleanup;

    if ((status = rlLaserArmLaser(handle, true)) != rlSUCCESS) goto Cleanup;

    while (1)
    {
        status = markSquare(handle);  // Function name retained as markSquare for uniformity
        if (status != rlSUCCESS)
            goto Cleanup;
    }

Cleanup:
    if (status != rlSUCCESS)
        printLastError();

    printf("Disconnecting from card...\n");
    if (rlDisconnect(handle) != rlSUCCESS)
        return printLastError();

    printf("Exiting with status = %d\n", status);
    return status;
}

static rlResult markSquare(rlHandle handle)
{
    rlResult result;
    double outerRadius = 750000;
    double innerRadius = 375000;
    int points = 5;
    double jumpSpeed = 30.0;
    double markSpeed = 1.0;

    int listIndex = 0;
    rlCommandListHandle list = rlListAllocate(handle);

    if ((result = rlListAppendPower(list, 65535)) != rlSUCCESS) return result;
    if ((result = rlListAppendJumpSpeed(list, jumpSpeed)) != rlSUCCESS) return result;
    if ((result = rlListAppendMarkSpeed(list, markSpeed)) != rlSUCCESS) return result;

    for (int i = 0; i <= points * 2; ++i)
    {
        double angle = M_PI * i / points;
        double r = (i % 2 == 0) ? outerRadius : innerRadius;
        double x = r * cos(angle);
        double y = r * sin(angle);
        if ((result = rlListAppendJumpAbs2D(list, x, y)) != rlSUCCESS) return result;
    }

    if ((result = rlListSet(handle, listIndex, list, false, -1)) != rlSUCCESS) return result;
    if ((result = rlListExecute(handle, listIndex)) != rlSUCCESS) return result;

    if ((result = rlListDelete(handle, listIndex, true)) != rlSUCCESS) return result;
    return rlListReleaseHandle(list);
}

static int printLastError(void)
{
    char errBuffer[1024] = {0};
    rlGetLastError(errBuffer, sizeof(errBuffer) - 1);
    printf("%s", errBuffer);
    return rlERROR;
}
