import timeit, os

mrcs_loc = ""
link_loc = ""
num_mrcs = 200


# TODO: Somehow eliminate the effects of disk caching
def linktest(use_syscall):
    links = []
    for i in range(num_mrcs):
        mrc_name = "{}/{}.mrc".format(mrcs_loc, i)
        link_name = "{}/{}.mrc".format(link_loc, i)
        links[i] = link_name
        if use_syscall:
            os.symlink(mrc_name, link_name)
        else:
            os.system("ln -s {} {}".format(link_name, link_name))

    # Clean up
    [os.unlink(link) for link in links]


if __name__ == "__main__":
    print(timeit.timeit("linktest(False)", setup="from __main__ import linktest()"))
    print(timeit.timeit("linktest(True)", setup="from __main__ import linktest()"))
