// Source: https://github.com/switchbrew/libnx/blob/master/nx/include/switch/result.h

R_DEFINE_NAMESPACE_RESULT_MODULE(libnx, 345);

namespace libnx {

    R_DEFINE_ERROR_RESULT(BadReloc, 1);
    R_DEFINE_ERROR_RESULT(OutOfMemory, 2);
    R_DEFINE_ERROR_RESULT(AlreadyMapped, 3);
    R_DEFINE_ERROR_RESULT(BadGetInfoStack, 4);
    R_DEFINE_ERROR_RESULT(BadGetInfoHeap, 5);
    R_DEFINE_ERROR_RESULT(BadQueryMemory, 6);
    R_DEFINE_ERROR_RESULT(AlreadyInitialized, 7);
    R_DEFINE_ERROR_RESULT(NotInitialized, 8);
    R_DEFINE_ERROR_RESULT(NotFound, 9);
    R_DEFINE_ERROR_RESULT(IoError, 10);
    R_DEFINE_ERROR_RESULT(BadInput, 11);
    R_DEFINE_ERROR_RESULT(BadReent, 12);
    R_DEFINE_ERROR_RESULT(BufferProducerError, 13);
    R_DEFINE_ERROR_RESULT(HandleTooEarly, 14);
    R_DEFINE_ERROR_RESULT(HeapAllocFailed, 15);
    R_DEFINE_ERROR_RESULT(TooManyOverrides, 16);
    R_DEFINE_ERROR_RESULT(ParcelError, 17);
    R_DEFINE_ERROR_RESULT(BadGfxInit, 18);
    R_DEFINE_ERROR_RESULT(BadGfxEventWait, 19);
    R_DEFINE_ERROR_RESULT(BadGfxQueueBuffer, 20);
    R_DEFINE_ERROR_RESULT(BadGfxDequeueBuffer, 21);
    R_DEFINE_ERROR_RESULT(AppletCmdIdNotFound, 22);
    R_DEFINE_ERROR_RESULT(BadAppletReceiveMessage, 23);
    R_DEFINE_ERROR_RESULT(BadAppletNotifyRunning, 24);
    R_DEFINE_ERROR_RESULT(BadAppletGetCurrentFocusState, 25);
    R_DEFINE_ERROR_RESULT(BadAppletGetOperationMode, 26);
    R_DEFINE_ERROR_RESULT(BadAppletGetPerformanceMode, 27);
    R_DEFINE_ERROR_RESULT(BadUsbCommsRead, 28);
    R_DEFINE_ERROR_RESULT(BadUsbCommsWrite, 29);
    R_DEFINE_ERROR_RESULT(InitFailSm, 30);
    R_DEFINE_ERROR_RESULT(InitFailAm, 31);
    R_DEFINE_ERROR_RESULT(InitFailHid, 32);
    R_DEFINE_ERROR_RESULT(InitFailFs, 33);
    R_DEFINE_ERROR_RESULT(BadGetInfoRng, 34);
    R_DEFINE_ERROR_RESULT(JitUnavailable, 35);
    R_DEFINE_ERROR_RESULT(WeirdKernel, 36);
    R_DEFINE_ERROR_RESULT(IncompatSysVer, 37);
    R_DEFINE_ERROR_RESULT(InitFailTime, 38);
    R_DEFINE_ERROR_RESULT(TooManyDevOpTabs, 39);
    R_DEFINE_ERROR_RESULT(DomainMessageUnknownType, 40);
    R_DEFINE_ERROR_RESULT(DomainMessageTooManyObjectIds, 41);
    R_DEFINE_ERROR_RESULT(AppletFailedToInitialize, 42);
    R_DEFINE_ERROR_RESULT(ApmFailedToInitialize, 43);
    R_DEFINE_ERROR_RESULT(NvinfoFailedToInitialize, 44);
    R_DEFINE_ERROR_RESULT(NvbufFailedToInitialize, 45);
    R_DEFINE_ERROR_RESULT(LibAppletBadExit, 46);
    R_DEFINE_ERROR_RESULT(InvalidCmifOutHeader, 47);
    R_DEFINE_ERROR_RESULT(ShouldNotHappen, 48);
    R_DEFINE_ERROR_RESULT(Timeout, 49);

}

R_DEFINE_NAMESPACE_RESULT_MODULE(libnx::binder, 349);

namespace libnx::binder {

    R_DEFINE_ERROR_RESULT(Unknown, 1);
    R_DEFINE_ERROR_RESULT(NoMemory, 2);
    R_DEFINE_ERROR_RESULT(InvalidOperation, 3);
    R_DEFINE_ERROR_RESULT(BadValue, 4);
    R_DEFINE_ERROR_RESULT(BadType, 5);
    R_DEFINE_ERROR_RESULT(NameNotFound, 6);
    R_DEFINE_ERROR_RESULT(PermissionDenied, 7);
    R_DEFINE_ERROR_RESULT(NoInit, 8);
    R_DEFINE_ERROR_RESULT(AlreadyExists, 9);
    R_DEFINE_ERROR_RESULT(DeadObject, 10);
    R_DEFINE_ERROR_RESULT(FailedTransaction, 11);
    R_DEFINE_ERROR_RESULT(BadIndex, 12);
    R_DEFINE_ERROR_RESULT(NotEnoughData, 13);
    R_DEFINE_ERROR_RESULT(WouldBlock, 14);
    R_DEFINE_ERROR_RESULT(TimedOut, 15);
    R_DEFINE_ERROR_RESULT(UnknownTransaction, 16);
    R_DEFINE_ERROR_RESULT(FdsNotAllowed, 17);

}

R_DEFINE_NAMESPACE_RESULT_MODULE(libnx::nv, 348);

namespace libnx::nv {

    R_DEFINE_ERROR_RESULT(Unknown, 1);
    R_DEFINE_ERROR_RESULT(NotImplemented, 2);
    R_DEFINE_ERROR_RESULT(NotSupported, 3);
    R_DEFINE_ERROR_RESULT(NotInitialized, 4);
    R_DEFINE_ERROR_RESULT(BadParameter, 5);
    R_DEFINE_ERROR_RESULT(Timeout, 6);
    R_DEFINE_ERROR_RESULT(InsufficientMemory, 7);
    R_DEFINE_ERROR_RESULT(ReadOnlyAttribute, 8);
    R_DEFINE_ERROR_RESULT(InvalidState, 9);
    R_DEFINE_ERROR_RESULT(InvalidAddress, 10);
    R_DEFINE_ERROR_RESULT(InvalidSize, 11);
    R_DEFINE_ERROR_RESULT(BadValue, 12);
    R_DEFINE_ERROR_RESULT(AlreadyAllocated, 13);
    R_DEFINE_ERROR_RESULT(Busy, 14);
    R_DEFINE_ERROR_RESULT(ResourceError, 15);
    R_DEFINE_ERROR_RESULT(CountMismatch, 16);
    R_DEFINE_ERROR_RESULT(SharedMemoryTooSmall, 17);
    R_DEFINE_ERROR_RESULT(FileOperationFailed, 18);
    R_DEFINE_ERROR_RESULT(IoctlFailed, 19);

}