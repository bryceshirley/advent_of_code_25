program dial_simulation_part2
    use dial_utils
    implicit none

    character(len=100) :: arg, input_file
    integer :: i, num_args, verbose_level, zero_lands
    integer :: n_lines
    integer, parameter :: MAX_LINES = 20000
    character(len=256), allocatable :: lines(:)
    logical :: file_found

    ! Initialize defaults
    input_file = ""
    verbose_level = 0
    file_found = .false.

    ! Parse Command Line Arguments
    num_args = command_argument_count()
    
    if (num_args < 1) then
        print *, "Usage: ./dial_sim_part2 <input_file> [-v] [-vv]"
        stop
    end if

    do i = 1, num_args
        call get_command_argument(i, arg)
        if (trim(arg) == "-v") then
            verbose_level = 1
        else if (trim(arg) == "-vv") then
            verbose_level = 2
        else
            input_file = trim(arg)
            file_found = .true.
        end if
    end do

    if (.not. file_found) then
        print *, "Error: No input file specified."
        stop 1
    end if

    ! Allocate line buffer
    allocate(lines(MAX_LINES))

    ! Read Input (new interface)
    call read_input(input_file, lines, MAX_LINES, n_lines)

    ! Execute Part 2 logic
    zero_lands = count_zero_lands_part2(lines(1:n_lines), verbose_level)

    ! Output results
    if (verbose_level > 0) then
        print *, "The dial pointed at 0 a total of ", zero_lands, " times (including mid-rotation)."
    else
        print *, zero_lands
    end if

end program dial_simulation_part2
