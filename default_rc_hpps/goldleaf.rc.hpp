// Source: https://github.com/XorTroll/Goldleaf/blob/master/Goldleaf/include/err/err_Result.hpp

R_DEFINE_NAMESPACE_RESULT_MODULE(goldleaf, 356);

namespace goldleaf {

    R_DEFINE_ERROR_RESULT(NotEnoughSize, 1);
    R_DEFINE_ERROR_RESULT(MetaNotFound, 2);
    R_DEFINE_ERROR_RESULT(CNMTNotFound, 3);
    R_DEFINE_ERROR_RESULT(TitleAlreadyInstalled, 4);
    R_DEFINE_ERROR_RESULT(EntryAlreadyPresent, 5);
    R_DEFINE_ERROR_RESULT(CouldNotLocateTitleContents, 6);
    R_DEFINE_ERROR_RESULT(CouldNotBuildNSP, 7);
    R_DEFINE_ERROR_RESULT(KeyGenMismatch, 8);
    R_DEFINE_ERROR_RESULT(InvalidNSP, 9);

}

R_DEFINE_NAMESPACE_RESULT_MODULE(goldleaf::errno, 357);

namespace goldleaf::errno {

    R_DEFINE_ERROR_RANGE(Errno, 1, 2000);

}