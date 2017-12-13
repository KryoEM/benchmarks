import timeit, os

mrcs_loc = "/home/ubuntu/local_test/Micrographs"
link_loc = "/home/ubuntu/local_test/Links"
num_mrcs = 100


# TODO: Somehow eliminate the effects of disk caching
def linktest(use_syscall):
    links = []
    for i in range(num_mrcs):
        mrc_name = "{}/{}.mrc".format(mrcs_loc, i)
        link_name = "{}/{}.mrc".format(link_loc, i)
        links.append(link_name)
        if not use_syscall:
            os.symlink(mrc_name, link_name)
        else:
            os.system("ln -s {} {}".format(mrc_name, link_name))

    # Clean up
    [os.unlink(link) for link in links]


if __name__ == "__main__":
    print("Running link test (os.symlink())")
    print("os.symlink(): {}\n".format(timeit.timeit("linktest(False)", setup="from __main__ import linktest", number=1)))
    print("Running link test (system call)")
    print("os.system(): {}".format(timeit.timeit("linktest(True)", setup="from __main__ import linktest", number=1)))
